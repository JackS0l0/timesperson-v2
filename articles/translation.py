from modeltranslation.translator import TranslationOptions,register
from .models import Articles,Categories,Contact,About,AboutinFooter
@register(AboutinFooter)
class AboutinFooterTranslationOptions(TranslationOptions):
    fields = ['txt']
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ['txt']
@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ['txt']
@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['name']
@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ['name','autor','txt','txt_desc']