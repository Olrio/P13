import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("lettings", "0002_auto_20230420_1047")]

    operations = [
        migrations.RunSQL("""
        insert into lettings_address select * from oc_lettings_site_address;
        """,
                          reverse_sql="""
                          delete from lettings_address;
                          """),
        migrations.RunSQL("""
        insert into lettings_letting select * from oc_lettings_site_letting;
        """,
                          reverse_sql="""
                          delete from lettings_letting;
                          """),
            ]
