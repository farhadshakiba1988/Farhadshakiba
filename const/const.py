from django.db import models


class Const(models.Model):
    key_map: dict = {
        1: 'department',
        2: 'job',
    }
    title = models.TextField(blank=True, null=True)
    k = models.SmallIntegerField()

    def __str__(self):
        return self.title

    @staticmethod
    def get(k: int, dep: int = None):
        q = Const.objects.filter(k=k)
        if dep is not None:
            q = q.filter(right__left_id__exact=dep)
        return [e for e in q.values()]

    @staticmethod
    def get_by_dep(dep: int):
        q = Const.objects.filter(right__left_id__exact=dep)
        return [e for e in q.values()]

    @staticmethod
    def get_by_name(k: str):
        key = list(Const.key_map.keys())[list(Const.key_map.values()).index(k)]
        return Const.get(key)


class Cdt(models.Model):
    left_id = models.ForeignKey(Const, related_name='left', on_delete=models.CASCADE)
    right_id = models.ForeignKey(Const, related_name='right', on_delete=models.CASCADE)
