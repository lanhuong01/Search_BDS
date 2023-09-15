import django_filters
from .models import BDS

class FilterBDS(django_filters.FilterSet):
	class Meta:
		model = BDS
		fields = ['news_type','range_price','range_size','city','direction','balcony_direction','legal','width','length',
		'bedrooms','toilets','floors','furniture']
