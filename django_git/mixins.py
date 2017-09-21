from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404


class OwnerOnlyRequiredMixin(LoginRequiredMixin, object):
	def get_object(self, **kwargs):
		user = self.request.user
		obj = super(OwnerOnlyRequiredMixin, self).get_object(**kwargs)

		if not obj.owner == user:
			raise PermissionDenied

		return obj

class OwnerRequiredMixin(LoginRequiredMixin, object):
	def get_object(self, **kwargs):
		user = self.request.user
		obj = super(OwnerRequiredMixin, self).get_object(**kwargs)

		owner = False
		if obj.owner == user:
			owner = True
		else:
			for editor in obj.editors.all():
				if editor.id == user.id:
					owner = True

		if owner == False:
			raise PermissionDenied

		return obj


class MultiSlugMixin(object):
	model = None

	def get_object(self, **kwargs):
		# slug from the url
		slug = self.kwargs.get("slug")
		ModelClass = self.model

		if slug is not None:
			try:
				obj = get_object_or_404(ModelClass, slug=slug)
			except ModelClass.MultipleObjectsReturned:
				obj = ModelClass.objects.filter(slug=slug).first()

		else:
			obj = super(MultiSlugMixin, self).get_object(**kwargs)
		return obj
