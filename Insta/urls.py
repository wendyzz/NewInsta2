"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from Insta.views import HelloDjango

urlpatterns = [
    path('', HelloDjango.as_view(), name='home'),
]