#!/bin/bash
# turan-welcome config
rm /usr/bin/turan-welcome
echo '#!/bin/bash' >> /usr/bin/turan-welcome
echo 'python3 /usr/share/turan/proqramlar/turan-welcome/welcome.py' >> /usr/bin/turan-welcome
chmod u+x /usr/bin/turan-welcome
