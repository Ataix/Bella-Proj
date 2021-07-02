from django.db import models


class Delivery(models.Model):
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


class AboutUs(models.Model):
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


class Contact(models.Model):
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


class WaysOfPayment(models.Model):
    """
    Contains information about payments
    """
    text_about_payment = models.TextField(verbose_name='Информациия об оплате')
    requisite_1 = models.CharField(max_length=60, verbose_name='Реквизит 1')
    requisite_2 = models.CharField(max_length=60, verbose_name='Реквизит 2')
    requisite_3 = models.CharField(max_length=60, verbose_name='Реквизит 3')


class QuestionAndAnswer(models.Model):
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


class ProductReturn(models.Model):
    """
    Contains information about product refund (return)
    """
    upward_text = models.TextField(
        verbose_name='Вверхний текст о возврате товара'
    )
    bottom_text = models.TextField(
        verbose_name='Нижний текст о возврате товара'
    )


class Requisite(models.Model):
    """
    Contains company's requisites
    """
    requisite_1 = models.CharField(max_length=60, verbose_name='Реквизит 1')
    requisite_2 = models.CharField(max_length=60, verbose_name='Реквизит 2')
    requisite_3 = models.CharField(max_length=60, verbose_name='Реквизит 3')


class PublicOffer(models.Model):
    """
    Characterize information about company's public offer
    """
    upward_text = models.TextField(verbose_name='Вверхний текст')
    bottom_text = models.TextField(verbose_name='Нижний текст')


class HowToMakeOrder(models.Model):
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
