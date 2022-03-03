"""
    Gets the information and links specific to each campus.
    The extra links for the campuses are different from those for the Rectory.
"""

campuses_info = {
    'informa': {
        'campus': 'reitori',
        'channel': '@ifb_informa',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/reitori',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'brasilia': {
        'campus': 'brasilia',
        'channel': '@ifb_cbra',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/brasilia',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'ceilandia': {
        'campus': 'campus-ceilandia',
        'channel': '@ifb_ccei',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/campus-ceilandia',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'estrutural': {
        'campus': 'campus-estrutural',
        'channel': '@ifb_cest',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/campus-estrutural',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'gama': {
        'campus': 'gama',
        'channel': '@ifb_cgam',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/gama',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'planaltina': {
        'campus': 'planaltina',
        'channel': '@ifb_cpla',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/planaltina',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'recanto': {
        'campus': 'recantodasemas',
        'channel': '@ifb_crem',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/recantodasemas',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'riacho': {
        'campus': 'riachofundo',
        'channel': '@ifb_crfi',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/riachofundo',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'samambaia': {
        'campus': 'samambaia',
        'channel': '@ifb_csam',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/samambaia',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'sao_sebastiao': {
        'campus': 'saosebastiao',
        'channel': '@ifb_cssb',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/saosebastiao',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
    'taguatinga': {
        'campus': 'taguatinga',
        'channel': '@ifb_ctag',
        'links': {
            'campus_news': 'https://www.ifb.edu.br/taguatinga',
            'portal_do_aluno_estagio': 'https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
            'portal_do_aluno_news': 'https://www.ifb.edu.br/portal-do-aluno/noticias',
            'estude_no_ifb_news': 'https://www.ifb.edu.br/estude-no-ifb/noticias'
        },
    },
}
