"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from Insta.views import PostView, PostDetail

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('post/<int:pk/', PostDetail.as_view(), name = 'post_detail'),
]