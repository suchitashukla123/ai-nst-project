import os
import torch
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField, FloatField, HiddenField
from PIL import Image
from torchvision import transforms

from utils.models import VGGEncoder, Decoder
from utils.utils import adaptive_instance_normalization


BASE_DIR = Path(__file__).resolve().parent
VGG_PATH = BASE_DIR / 'vgg_normalised.pth'
DECODER_PATH = BASE_DIR / 'experiment' / 'final_exp' / 'decoder_final.pth'
UPLOAD_FOLDER = BASE_DIR / 'static' / 'uploads'
EXAMPLES_FOLDER = BASE_DIR / 'examples'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
Bootstrap(app)

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


class UploadForm(FlaskForm):
    content = FileField('Content Image')
    style = FileField('Style Image')
    content_path = HiddenField()
    style_path = HiddenField()
    alpha = FloatField('Alpha', default=1.0)
    submit = SubmitField('Transfer Style')


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)

if not VGG_PATH.exists():
    raise FileNotFoundError(f'VGG file not found: {VGG_PATH}')

if not DECODER_PATH.exists():
    raise FileNotFoundError(f'Decoder file not found: {DECODER_PATH}')


encoder = VGGEncoder(str(VGG_PATH)).to(device)
decoder = Decoder().to(device)

decoder.load_state_dict(
    torch.load(str(DECODER_PATH), map_location=device)
)

encoder.eval()
decoder.eval()

print('Models loaded successfully!')


def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower()
        in app.config['ALLOWED_EXTENSIONS']
    )


def style_transfer(content_image, style_image, encoder, decoder, alpha, device):

    transform = transforms.Compose([
        transforms.Resize(512),
        transforms.ToTensor()
    ])

    content_image = transform(content_image).unsqueeze(0).to(device)
    style_image = transform(style_image).unsqueeze(0).to(device)

    alpha = max(0.0, min(1.0, float(alpha)))

    with torch.no_grad():

        content_feats = encoder(content_image, is_test=True)
        style_feats = encoder(style_image, is_test=True)

        stylized_feats = adaptive_instance_normalization(
            content_feats, style_feats
        )

        stylized_feats = (
            alpha * stylized_feats +
            (1 - alpha) * content_feats
        )

        stylized_image = decoder(stylized_feats)

    return stylized_image


def save_image(image, path):

    image = image.detach().cpu().squeeze(0).clamp(0, 1)
    image = transforms.ToPILImage()(image)
    image.save(path)


@app.route('/', methods=['GET', 'POST'])
def index():

    form = UploadForm()
    result_image = None
    content_filename = None
    style_filename = None
    error = None

    if form.validate_on_submit():

        if form.content.data and form.content.data.filename:

            if allowed_file(form.content.data.filename):

                content_filename = secure_filename(
                    form.content.data.filename
                )

                form.content.data.save(
                    str(UPLOAD_FOLDER / content_filename)
                )

                form.content_path.data = content_filename

            else:
                error = 'Invalid content image.'

        else:
            content_filename = form.content_path.data

        if form.style.data and form.style.data.filename:

            if allowed_file(form.style.data.filename):

                style_filename = secure_filename(
                    form.style.data.filename
                )

                form.style.data.save(
                    str(UPLOAD_FOLDER / style_filename)
                )

                form.style_path.data = style_filename

            else:
                error = 'Invalid style image.'

        else:
            style_filename = form.style_path.data

        if not error and content_filename and style_filename:

            try:

                content_path = UPLOAD_FOLDER / content_filename
                style_path = UPLOAD_FOLDER / style_filename

                content_image = Image.open(
                    content_path
                ).convert('RGB')

                style_image = Image.open(
                    style_path
                ).convert('RGB')

                alpha = (
                    form.alpha.data
                    if form.alpha.data is not None
                    else 1.0
                )

                result = style_transfer(
                    content_image,
                    style_image,
                    encoder,
                    decoder,
                    alpha,
                    device
                )

                result_filename = 'stylized_' + content_filename
                result_path = UPLOAD_FOLDER / result_filename

                save_image(result, result_path)

                result_image = result_filename

            except Exception as e:
                error = str(e)

        elif not content_filename:
            error = 'Please upload content image.'

        elif not style_filename:
            error = 'Please upload style image.'

    return render_template(
        'index.html',
        form=form,
        result_image=result_image,
        content_image=content_filename,
        style_image=style_filename,
        error=error
    )


@app.route('/uploads/<filename>')
def send_image(filename):
    return send_from_directory(
        str(UPLOAD_FOLDER), filename
    )


@app.route('/examples/<path:filename>')
def send_example(filename):
    return send_from_directory(
        str(EXAMPLES_FOLDER), filename
    )


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )






