def _calc_signature(raw, key):
    hashed = hmac.new(key, raw, hashlib.sha1)
    return hashed.digest().encode("base64").rstrip('\n')


def _verify_mandrill_signature(request, key):
    mandrill_signature = request.META['HTTP_X_MANDRILL_SIGNATURE']
    signed_data = request.build_absolute_uri()
    for k in sorted(request.POST.keys()):
        signed_data += k
        signed_data += request.POST[k]
    return mandrill_signature == _calc_signature(signed_data, key)


def verify_mandrill_signature(key):
    def verify_mandrill_signature_decorator(func):
        def func_wrapper(request):
            if _verify_mandrill_signature(request, key):
                return func(request)
            return HttpResponse(status=403)
        return func_wrapper
    return verify_mandrill_signature_decorator
    
'''
EXAMPLE
'''
@verify_mandrill_signature(settings.MANDRILL_SENT_WEBHOOK_KEY)
def webhook_message_is_sent(request):
  pass
