from model_mommy.recipe import Recipe, seq
from url_services.models import UrlShortener

url_shortener = Recipe(UrlShortener,
                       url_shortener_id=seq(1),
                       absolute_url='www.smartbeans.com.br',
                       short_url='a3b4c5')
