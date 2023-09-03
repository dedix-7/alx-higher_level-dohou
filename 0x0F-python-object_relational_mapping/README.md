#### Python ORM (Object Relational Mapping)

In this directory, I learn Object Relational Mapping with Python, and handling MySQL databases using SQLAlchemy and other technologies.


### Difference between from sqlalchemy.ext.declarative import declarative_base' and 'from sqlalchemy.orm import declarative_base'

---

Both `from sqlalchemy.ext.declarative import declarative_base` and `from sqlalchemy.orm import declarative_base` provide functionality to declare base classes in SQLAlchemy from which mapped classes can be defined. However, their availability and purpose vary depending on the version of SQLAlchemy you're using.

1. **`from sqlalchemy.ext.declarative import declarative_base`**:
   - This is the traditional way of importing `declarative_base` in SQLAlchemy versions prior to 1.4.
   - In versions 1.4 and above, this still works but is considered legacy. The newer version of SQLAlchemy started a transition into a unified core and ORM API, which led to the introduction of the new import path.

2. **`from sqlalchemy.orm import declarative_base`**:
   - Starting from SQLAlchemy 1.4, this is the new recommended way to import `declarative_base`.
   - This path is in line with the changes introduced in version 1.4, where SQLAlchemy started to provide more consistent and unified methods for both ORM and core functionalities.

If you're using SQLAlchemy 1.4 or newer, it's recommended to use `from sqlalchemy.orm import declarative_base`. If you're on an older version, you'll need to use `from sqlalchemy.ext.declarative import declarative_base`.

It's always a good idea to refer to the documentation or check the available modules in your installed version of SQLAlchemy if you're unsure about the import paths.

---

## SQLAlchemy `declarative_base` Import Paths

In SQLAlchemy, the `declarative_base` function is used to declare a base class from which other mapped classes can be defined. Depending on the version of SQLAlchemy you're using, there are different recommended import paths.

### Traditional Import (Prior to SQLAlchemy 1.4)

Before SQLAlchemy version 1.4, the traditional way to import `declarative_base` is:

```markdown
from sqlalchemy.ext.declarative import declarative_base
```

This method is still functional in versions 1.4 and above but is considered legacy.

### New Import (From SQLAlchemy 1.4 Onwards)

Starting from SQLAlchemy 1.4, there's a new recommended way to import `declarative_base` due to the transition into a unified core and ORM API:

```markdown
from sqlalchemy.orm import declarative_base
```

This path aligns with the changes in the newer version, aiming to provide a more consistent approach for both ORM and core functionalities.

**Recommendation**:
- If you're using SQLAlchemy 1.4 or newer, opt for `from sqlalchemy.orm import declarative_base`.
- If you're on an older version, stick with `from sqlalchemy.ext.declarative import declarative_base`.

Always refer to the official SQLAlchemy documentation or inspect your installed version if unsure about the import paths.

---
