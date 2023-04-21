import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("profiles", "0001_initial")]

    operations = [
        migrations.RunSQL("""
        insert into profiles_profile select * from oc_lettings_site_profile;
        """,
                          reverse_sql="""
                          delete from profiles_profile;
                          """)
            ]
