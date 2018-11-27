==================
HR Attendance RFID
==================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fhr-lightgray.png?logo=github
    :target: https://github.com/OCA/hr/tree/12.0/hr_attendance_rfid
    :alt: OCA/hr
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/hr-12-0/hr-12-0-hr_attendance_rfid
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/116/12.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module extends the functionality of HR Attendance in order to allow
the logging of employee attendances using an RFID based employee
attendance system.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To use this module, you need to use an external system that calls the method
'register_attendance' of the model 'hr.employee' passing as parameter the
code of the RFID card.

Developers of a compatible RFID based employee attendance system should
be familiar with the outputs of this method and implement proper calls and
management of responses.

It is advisory to create an exclusive user to perform this task. As
user doesn't need several access, it is just essential to perform the check
in/out, a group has been created. Add your attendance device user to
RFID Attendance group.

Usage
=====

#. The HR employee responsible to set up new employees should go to
   'Attendances -> Manage Attendances -> Employees' and register the
   RFID card code of each of your employees. You can use an USB plugged
   RFID reader connected to your computer for this purpose.
#. The employee should put his/her card to the RFID based employee
   attendance system. It is expected that the system will provide some form
   of output of the registration event.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/hr/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/hr/issues/new?body=module:%20hr_attendance_rfid%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Comunitea
* Eficent

Contributors
~~~~~~~~~~~~

* Omar Catiñeira Saavedra <omar@comunitea.com>
* Héctor Villarreal Ortega <hector.villarreal@eficent.com>
* Jordi Ballester Alomar <jordi.ballester@eficent.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/hr <https://github.com/OCA/hr/tree/12.0/hr_attendance_rfid>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.