from flask import Blueprint, render_template, request
from pokemon.models import Pokemon
from pokemon.extensions import db

core_bp = Blueprint('core', __name__, template_folder='templates')

@core_bp.route('/')
def index():
    page = request.args.get('page', default=1, type=int)  # ✅ กัน None
    query = db.select(Pokemon).order_by(Pokemon.id.desc())  # ✅ เรียงให้คงที่ (ถ้ามี id)

    pokemons = db.paginate(query, page=page, per_page=4, error_out=False)  # ✅ กัน page เกิน/พัง
    return render_template(
        'core/index.html',
        title='Home Page',
        pokemons=pokemons
    )