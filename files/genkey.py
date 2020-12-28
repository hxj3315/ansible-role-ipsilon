#!/usr/bin/python
import time
import os.path

from jwcrypto.jwk import JWK, JWKSet

keyid = int(time.time())
keyset = JWKSet()
rsasig = JWK(generate='RSA', size=2048, use='sig',
             kid='%s-sig' % keyid)
keyset.add(rsasig)
rsasig = JWK(generate='RSA', size=2048, use='enc',
             kid='%s-enc' % keyid)
keyset.add(rsasig)

if not os.path.exists('/var/lib/ipsilon/idp/openidc'):
  os.makedirs('/var/lib/ipsilon/idp/openidc')

with open('/var/lib/ipsilon/idp/openidc/openidc.key', 'w') as m:
    m.write(keyset.export())
