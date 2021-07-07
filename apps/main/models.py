from django.db import models

from apps.main.singleton_model import SingletonModel


class Delivery(SingletonModel):
    """
    Characterize static information about delivery
    """
    upward_text = models.TextField(verbose_name='Вверхний текст о доставке')
    upward_img = models.ImageField(
        upload_to='main_static', verbose_name='Вверхнее фото о доставке'
    )
    bottom_text = models.TextField(verbose_name='Нижний текст о доставке')
    bottom_img = models.ImageField(
        upload_to='main_static', verbose_name='Ниэнее фото о доставке'
    )

    def __unicode__(self):
        return u'Доставка'

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'


class AboutUs(SingletonModel):
    """
    Characterize static information about company
    """
    left_up_img = models.ImageField(
        upload_to='main_static', verbose_name='Вверхнее левое фото о компании'
    )
    right_down_img = models.ImageField(
        upload_to='main_static', verbose_name='Нижнее правое фото о компании'
    )
    upward_text = models.TextField(verbose_name='Ввержний текст о компании')
    bottom_text = models.TextField(verbose_name='Нижниий текст о компании')

    def __unicode__(self):
        return u'О Нас'

    class Meta:
        verbose_name = 'О Нас'
        verbose_name_plural = 'О Нас'


class Contact(SingletonModel):
    """
    Represent information about how to contact company
    """
    phone_number = models.CharField(
        max_length=20, verbose_name='Контакнтый номер компании'
    )
    email = models.EmailField(
        verbose_name='Контакная электронная почта компании'
    )
    address = models.CharField(max_length=50, verbose_name='Адрес компании')
    odnoklassniki = models.CharField(
        max_length=60, verbose_name="Профиль компании в 'Одноклассниках'"
    )
    vkontakte = models.CharField(
        max_length=60, verbose_name="Профиль компании в 'Вконтакте'"
    )
    instagram = models.CharField(
        max_length=60, verbose_name="Профиль компании в 'Instagram'"
    )
    facebook = models.CharField(
        max_length=60, verbose_name="Профиль компании в 'Facebook'"
    )

    def __unicode__(self):
        return u'Контакты'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class WaysOfPayment(SingletonModel):
    """
    Contains information about payments
    """
    text_about_payment = models.TextField(verbose_name='Информациия об оплате')
    requisite_1 = models.CharField(max_length=60, verbose_name='Реквизит 1')
    requisite_2 = models.CharField(max_length=60, verbose_name='Реквизит 2')
    requisite_3 = models.CharField(max_length=60, verbose_name='Реквизит 3')

    def __unicode__(self):
        return u'Способы оплаты'

    class Meta:
        verbose_name = 'Способы оплаты'
        verbose_name_plural = 'Способы оплаты'


class QuestionAndAnswer(SingletonModel):
    """
    Characterize customers' questions and company's response to questions
    """
    upward_question = models.CharField(
        max_length=60, verbose_name='Вверхний вопрос'
    )
    upward_answer = models.TextField(verbose_name='Нижний вопрос')
    bottom_question = models.CharField(
        max_length=60, verbose_name='Ответ на верхний вопрос'
    )
    bottom_answer = models.TextField(verbose_name='Ответ на нижний вопрос')

    def __unicode__(self):
        return u'Вопросы и Ответы'

    class Meta:
        verbose_name = 'Вопросы и Ответы'
        verbose_name_plural = 'Вопросы и Ответы'


class ProductReturn(SingletonModel):
    """
    Contains information about product refund (return)
    """
    upward_text = models.TextField(
        verbose_name='Вверхний текст о возврате товара'
    )
    bottom_text = models.TextField(
        verbose_name='Нижний текст о возврате товара'
    )

    def __unicode__(self):
        return u'Возврат Товара'

    class Meta:
        verbose_name = 'Возврат Товара'
        verbose_name_plural = 'Возврат Товара'


class Requisite(SingletonModel):
    """
    Contains company's requisites
    """
    requisite_1 = models.CharField(max_length=60, verbose_name='Реквизит 1')
    requisite_2 = models.CharField(max_length=60, verbose_name='Реквизит 2')
    requisite_3 = models.CharField(max_length=60, verbose_name='Реквизит 3')

    def __unicode__(self):
        return u'Реквизиты'

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'


class PublicOffer(SingletonModel):
    """
    Characterize information about company's public offer
    """
    upward_text = models.TextField(verbose_name='Вверхний текст')
    bottom_text = models.TextField(verbose_name='Нижний текст')

    def __unicode__(self):
        return u'Публичная Оферта'

    class Meta:
        verbose_name = 'Публичная Оферта'
        verbose_name_plural = 'Публичная Оферта'


class HowToMakeOrder(SingletonModel):
    """
    Contains information about making an offer
    """
    upward_text = models.TextField(
        verbose_name='Вверхний текст об оформлении заказа'
    )
    upward_img = models.ImageField(
        upload_to='main_static',
        verbose_name='Вверхнее фото об оформлении заказа'
    )
    bottom_text = models.TextField(
        verbose_name='Нижний текст об оформлении заказа'
    )
    bottom_img = models.ImageField(
        upload_to='main_static',
        verbose_name='Нижнее фото об оформлении заказа'
    )

    def __unicode__(self):
        return u'Как Сделать Заказ'

    class Meta:
        verbose_name = 'Как Сделать Заказ'
        verbose_name_plural = 'Как Сделать Заказ'


class News(models.Model):
    """
    Model that characterize company's news
    """
    title = models.CharField(max_length=60, verbose_name='Заголовок новости')
    create_date = models.DateTimeField(
        auto_created=True, verbose_name='Дата создания новости'
    )
    description = models.TextField(verbose_name='Текст новости')
    image = models.ImageField(
        upload_to='news_img', verbose_name='Изображение новости'
    )

    def __str__(self):
        return f'{self.title} on {self.create_date}'
