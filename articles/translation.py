from modeltranslation.translator import TranslationOptions,register
from .models import Articles,Categories
@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['name']
@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ['name','autor','txt','txt_desc']