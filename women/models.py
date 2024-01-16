from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from common.translit import translit_to_eng


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, "Черновик")
        PUBLISHED = (1, "Опубликовано")

    title = models.CharField("Имя", max_length=255)
    slug = models.SlugField("URL", max_length=255, unique=True, db_index=True)
    photo = models.ImageField("Фото", upload_to="photos/%Y/%m/%d", default=None, blank=True, null=True)
    content = models.TextField("Биография", blank=True)
    time_created = models.DateTimeField("Дата создание", auto_now_add=True)
    time_updated = models.DateTimeField("Дата изменение", auto_now=True)
    is_published = models.BooleanField("Статус",
                                       choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Категории")
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name="Теги")
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True, blank=True, related_name='men',
                                   verbose_name="Муж")

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.title))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-time_created',)
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'

        indexes = [
            models.Index(fields=['-time_created'])
        ]

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField("Категория", max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(null=True)
    m_count = models.PositiveSmallIntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
