from fanstatic import Library, Resource
from js.backbone import backbone
from js.jquery import jquery
from js.underscore import underscore
from js.json2 import json2

__import__('pkg_resources').declare_namespace(__name__)

library = Library('backbone.marionette.js', 'resources')
marionette = Resource(library,
    'backbone.marionette.min.js',
    debug="backbone.marionette.js",
    depends=[backbone, jquery, underscore, json2])
