from django.db import models

class Card(models.Model):
    CARD_ATT = {
        ('일반몬스터', '일반몬스터'),
        ('효과몬스터', '효과몬스터'),
        ('일반마법', '일반마법'),
        ('필드마법', '필드마법'),
        ('함정', '함정'),
        ('레전드', '레전드')
    }
    CARD_ELE = {
        ('빛', '빛'),
        ('어둠', '어둠'),
        ('화염', '화염'),
        ('물', '물'),
        ('땅', '땅'),
        ('바람', '바람'),
        ('마법', '마법'),
        ('함정', '함정')
    }
    CARD_TYPE = {
        ('곤충족', '곤충족'),
        ('공룡족', '공룡족'),
        ('기계족', '기계족'),
        ('드래곤족', '드래곤족'),
        ('마법사족', '마법사족'),
        ('물족', '물족'),
        ('번개족', '번개족'),
        ('비행야수족', '비행야수족'),
        ('사이버스족', '사이버스족'),
        ('사이킥족', '사이킥족'),
        ('악마족', '악마족'),
        ('암석족', '암석족'),
        ('야수족', '야수족'),
        ('야수전사족', '야수전사족'),
        ('어류족', '어류족'),
        ('언데드족', '언데드족'),
        ('전사족', '전사족'),
        ('천사족', '천사족'),
        ('파충류족', '파충류족'),
        ('해룡족', '해룡족'),
        ('화염족', '화염족'),
        ('마법', '마법'),
        ('함정', '함정'),
    }
    card_id = models.CharField(max_length=50, primary_key=True)
    card_name = models.CharField(max_length=50)
    card_attribute = models.CharField(max_length=50, choices=CARD_ATT)
    card_element = models.CharField(max_length=50, choices=CARD_ELE)
    card_level = models.IntegerField(default=0)
    card_type = models.CharField(max_length=50, choices=CARD_TYPE)
    card_text = models.TextField(max_length=200)
    card_ATK = models.IntegerField(default=0)
    card_DEF = models.IntegerField(default=0)

# Create your models here.
