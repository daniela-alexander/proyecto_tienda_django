import logging
from django.shortcuts import render

# Create your views here.
logger = logging.getLogger(__name__)

def home(request) :
    logger.info(
"Home page requested"
)
    
    return render(request, "core/home.html")