# -*- coding: utf-8 -*-

from pywe_membercard import MemberCard, get_activate_url, get_miniapp_extraData

from local_wecfg_example import MEMBER_CARD_ID, WECHAT


class TestMediaCommands(object):

    def test_get_activate_url(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        membercard = MemberCard(appid=appid, secret=appsecret)
        data = membercard.get_activate_url(MEMBER_CARD_ID, 'test')
        # {u'errcode': 0,
        #  u'errmsg': u'ok',
        #  u'url': u'https://mp.weixin.qq.com/bizmall/activatemembercard?action=preshow&&encrypt_card_id=encrypt_card_id&outer_str=outer_str&biz=biz#wechat_redirect'}
        assert isinstance(data, dict)
        assert data.get('url', '')

        data = get_activate_url(MEMBER_CARD_ID, 'test', appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('url', '')

    def test_get_miniapp_extraData(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        membercard = MemberCard(appid=appid, secret=appsecret)
        data = membercard.get_miniapp_extraData(MEMBER_CARD_ID, 'test')
        assert isinstance(data, dict)
        assert data.get('encrypt_card_id', '')

        data = get_miniapp_extraData(MEMBER_CARD_ID, 'test', appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('encrypt_card_id', '')
