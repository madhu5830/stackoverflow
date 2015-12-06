from django.shortcuts import render

from .models import Post, Category, Thread, Forum, Settings, Cursor, Response, Threaddata, Feature, Forumdata, Session

from .serializers import PostSerializer, ThreadSerializer,CursorSerializer,ResponseSerializer,ThreaddataSerializer, SettingsSerializer, ForumSerializer, FeatureSerializer, SessionSerializer, ForumdataSerializer

from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class CursorViewSet(viewsets.ModelViewSet):
    queryset = Cursor.objects.all()
    serializer_class = CursorSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class ThreaddataViewSet(viewsets.ModelViewSet):
    queryset = Threaddata.objects.all()
    serializer_class = ThreaddataSerializer

class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ForumdataViewSet(viewsets.ModelViewSet):
    queryset = Forumdata.objects.all()
    serializer_class = ForumdataSerializer




#javascript
class Jav(View):
    def get(self, request):
        return render(request, 'onboard.load.74629aaa32655c2e6f4b24ea139b9588.js')

class Java(View):
    def get(self, request):
        return render(request, 'lounge.load.104feca2c767b6d7ee0b10d93beeec41.js')

class Sty(View):
    def get(self, request):
        return render(request, 'loading.aaa873ed4a78106f29994d34d7eabec1.css')

class Javar(View):
    def get(self, request):
        return render(request, 'onboard.bundle.acb5cc31dd9945f747781741d77c3ca0.js')

class Styl(View):
    def get(self, request):
        return render(request, 'onboard.2506c1ec14ef8f1458ce7e1a5c25b41e.css')

class Style(View):
    def get(self, request):
        return render(request, 'onboard_rtl.8e4c4b668a1e7a0802e1803103266a67.css')
    
class Javasr(View):
    def get(self, request):
        return render(request, 'common.bundle.ea27411799c4b519ccba088d8128f69b.js')

class Javascr(View):
    def get(self, request):
        return render(request, 'discovery.bundle.7e1ddeee2389924c7bd81848bd4b2811.js')

class Javascri(View):
    def get(self, request):
        return render(request, 'highlight.0faa05361b05582ff85f4eff7fda997e.js')

class Javascrip(View):
    def get(self, request):
        return render(request, 'alfie.f51946af45e0b561c60f768335c9eb79.js')

class Javascript(View):
    def get(self, request):
        return render(request, 'lounge.bundle.2e1b127fc3fbc843564151b8659f9265.js')

class Styler(View):
    def get(self, request):
        return render(request, 'lounge.fcc2aae7ac79584a0849157bcc4b0f37.css')
    
class Styleri(View):
    def get(self, request):
        return render(request, 'lounge_rtl.ee9161fd5bc5db11769dcef8c444bbd9.css')

class Styleris(View):
    def get(self, request):
        return render(request, 'discovery.1fe89d176a9928445563cdce9d8680d4.css')

class Stylerist(View):
    def get(self, request):
        return render(request, 'discovery_rtl.916d71fb6963105e91d0516bd34ad29a.css')

class Javascripti(View):
    def get(self, request):
        return render(request, 'adclient.bundle.9e7c14d0b6675e0a0d79a343c80a0b8a.js')

