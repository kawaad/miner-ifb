class Channels:
    """
        Gets the information and links specific to each campus.
        The extra links for the campuses are different from those for the Rectory.
    """

    channels_dict = {
        'informa': {
            'campus': 'reitori',
            'channel': '@ifb_informa',
            'links': ['https://www.ifb.edu.br/reitori',
                      'https://www.ifb.edu.br/estude-no-ifb/noticias'],
        },
        'brasilia': {
            'campus': 'brasilia',
            'channel': '@ifb_cbra',
            'links': ['https://www.ifb.edu.br/brasilia', ],
        },
        'ceilandia': {
            'campus': 'campus-ceilandia',
            'channel': '@ifb_ccei',
            'links': ['https://www.ifb.edu.br/campus-ceilandia', ],
        },
        'estrutural': {
            'campus': 'campus-estrutural',
            'channel': '@ifb_cest',
            'links': ['https://www.ifb.edu.br/campus-estrutural', ],
        },
        'gama': {
            'campus': 'gama',
            'channel': '@ifb_cgam',
            'links': ['https://www.ifb.edu.br/gama', ],
        },
        'planaltina': {
            'campus': 'planaltina',
            'channel': '@ifb_cpla',
            'links': ['https://www.ifb.edu.br/planaltina', ],
        },
        'recanto': {
            'campus': 'recantodasemas',
            'channel': '@ifb_crem',
            'links': ['https://www.ifb.edu.br/recantodasemas', ],
        },
        'riacho': {
            'campus': 'riachofundo',
            'channel': '@ifb_crfi',
            'links': ['https://www.ifb.edu.br/riachofundo', ],
        },
        'samambaia': {
            'campus': 'samambaia',
            'channel': '@ifb_csam',
            'links': ['https://www.ifb.edu.br/samambaia', ],
        },
        'sao_sebastiao': {
            'campus': 'saosebastiao',
            'channel': '@ifb_cssb',
            'links': ['https://www.ifb.edu.br/saosebastiao', ],
        },
        'taguatinga': {
            'campus': 'taguatinga',
            'channel': '@ifb_ctag',
            'links': ['https://www.ifb.edu.br/taguatinga', ],
        },
    }

    CAMPI_LINKS = ['https://www.ifb.edu.br/portal-do-aluno/estagio/boletins-de-estagio',
                   'https://www.ifb.edu.br/portal-do-aluno/noticias',
                   'https://www.ifb.edu.br/estude-no-ifb/noticias']

    def get_channels_info(self):
        for channel in self.channels_dict:
            info = self.channels_dict.get(channel)
            if 'reitori' in info['campus']:
                continue
            self.build_campi_links(campus_info=info)
        return self.channels_dict

    def build_campi_links(self, campus_info):
        for link in self.CAMPI_LINKS:
            campus_info['links'].append(link)


if __name__ == "__main__":
    channels = Channels()
    channels.get_channels_info()
