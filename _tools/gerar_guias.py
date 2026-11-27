#!/usr/bin/env python3
"""Gera as páginas de guia estáticas (Carteira Predial e Estoque Inteligente), o sitemap.xml e o robots.txt.

Uso: python3 _tools/gerar_guias.py   (a partir da raiz do repositório)
O conteúdo fica em PAGINAS abaixo; edite aqui e rode de novo.
"""
import html
import json
import os
from datetime import date

SITE = "https://mfagentes.com.br"
HOJE = date.today().isoformat()
ATUALIZADO = "Atualizado em novembro de 2026"

WA_CARTEIRA = (
    "https://wa.me/551131974420?text=Ol%C3%A1%21%20Quero%20participar%20do%20piloto%20da%20Carteira%20Predial."
    "%0AMeu%20nome%3A%20%0AQuantos%20pr%C3%A9dios%20administro%3A%20%0ACidade%3A%20"
)
ESTOQUE_REG = "https://estoque.mfagentes.com.br/register"

CTA = {
    "carteira": {
        "titulo": "Controle todos os prazos da sua carteira em um só lugar",
        "texto": "A Carteira Predial reúne manutenções, obrigações legais, contratos e visitas de todos os prédios que você administra, com alertas antes de cada vencimento. Importe e exporte tudo em Excel. Estamos em piloto com síndicos profissionais.",
        "botao": "Quero participar do piloto",
        "href": WA_CARTEIRA,
    },
    "estoque": {
        "titulo": "Estoque sem planilha e sem contar tudo na mão",
        "texto": "No Estoque Inteligente você fotografa a nota fiscal, a prateleira ou o caderno onde anota hoje, e a IA lê os itens para você confirmar. O estoque se atualiza sozinho, a tela inicial mostra o que fazer no dia e a lista de compras sai pronta, com o custo estimado.",
        "botao": "Pedir acesso",
        "href": ESTOQUE_REG,
    },
}

AVISO_LEGAL = (
    "Este guia é informativo e resume normas e práticas comuns. As exigências mudam de estado para estado e de cidade para cidade, "
    "e as normas técnicas são atualizadas. Confira sempre a legislação do seu município e do seu estado, as instruções do Corpo de Bombeiros "
    "local e a orientação de um profissional habilitado."
)

PAGINAS = [
    # ---------------- Carteira Predial ----------------
    {
        "caminho": "condominio/manutencoes-obrigatorias/",
        "app": "carteira",
        "title": "Manutenções obrigatórias do condomínio: calendário do síndico | MF Agentes",
        "h1": "Manutenções obrigatórias do condomínio: o calendário do síndico",
        "descricao": "Calendário com as principais manutenções e laudos do condomínio: extintores, hidrantes, bombas, caixa d'água, para-raios, AVCB e mais, com a frequência de cada um.",
        "lead": "Esquecer um prazo de manutenção pode custar a renovação do AVCB, criar problema com o seguro e deixar o síndico exposto. Veja as rotinas mais comuns e com que frequência cada uma costuma ser feita.",
        "secoes": [
            ("Por que manter um plano de manutenção", [
                "A norma ABNT NBR 5674 trata da gestão da manutenção de edificações. Ela pede um programa de manutenção feito para o prédio, com o que será verificado, com que frequência e por quem, e um registro de cada serviço feito (data e o que foi realizado).",
                "Esse histórico é o que comprova que o condomínio cuidou do prédio. Ele ajuda na vistoria dos bombeiros, na conversa com o seguro e na prestação de contas para os condôminos.",
            ]),
        ],
        "tabela": {
            "titulo": "Frequências mais comuns",
            "colunas": ["Item", "Frequência usual", "Observação"],
            "linhas": [
                ["Portas corta-fogo", "Mensal", "Fechamento automático, molas e vedação."],
                ["Hidrantes e sinalização de emergência", "Mensal", "Registros, esguichos e placas visíveis."],
                ["Pressurização de escadas (se houver)", "Mensal", "Teste de funcionamento."],
                ["Bombas de incêndio", "Trimestral", "Teste de partida e pressão."],
                ["Detecção e alarme de incêndio", "Trimestral", "Teste dos acionadores e da central."],
                ["Sprinklers (se houver)", "Trimestral", "Válvulas e pressão da rede."],
                ["Iluminação de emergência", "Semestral", "Autonomia das baterias."],
                ["Limpeza da caixa d'água", "Semestral (mínimo anual)", "Com empresa especializada e comprovante."],
                ["Extintores", "Anual", "Inspeção e recarga por empresa certificada."],
                ["Mangueiras de incêndio", "Anual", "Inspeção e ensaio."],
                ["Para-raios (SPDA)", "A cada 3 anos (1 ano em áreas de corrosão severa, como o litoral)", "Inspeção completa com laudo e ART."],
                ["AVCB", "Conforme a validade do certificado", "Comece a renovação com meses de antecedência."],
            ],
            "nota": "Frequências usuais de mercado e das normas técnicas mais citadas. O plano do seu prédio pode exigir prazos menores, conforme o manual do proprietário, os equipamentos instalados e as regras locais.",
        },
        "secoes_depois": [
            ("Elevadores, dedetização e outros contratos", [
                "Elevadores normalmente têm manutenção mensal feita por empresa habilitada, e muitas cidades têm lei própria sobre isso. Dedetização, desratização, limpeza de calhas, gerador e portões também entram no plano, com a frequência definida no contrato ou pela vigilância sanitária local.",
            ]),
            ("Como não perder nenhum prazo", [
                "Monte uma lista única por prédio com o item, a data do último serviço, a próxima data e o fornecedor. Guarde junto os certificados, laudos e ARTs.",
                "Quem administra vários prédios precisa enxergar tudo de uma vez, com alerta antes de cada vencimento. É exatamente para isso que a Carteira Predial foi criada.",
            ]),
        ],
        "faq": [
            ("A NBR 5674 é lei?", "É uma norma técnica da ABNT. Normas técnicas são usadas como referência pelo Corpo de Bombeiros, por peritos e pela Justiça, e várias leis e decretos fazem referência a elas. Na prática, segui-las protege o condomínio e o síndico."),
            ("Quem é responsável pelas manutenções?", "O síndico responde pela conservação das áreas comuns (Código Civil, art. 1.348). Ele pode contar com zelador e empresas contratadas, mas cabe a ele garantir que o plano seja cumprido e documentado."),
            ("Onde encontro as frequências do meu prédio?", "No manual do proprietário e de uso e manutenção entregue pela construtora, nos contratos com fornecedores e nas exigências do Corpo de Bombeiros do seu estado."),
        ],
        "relacionados": ["condominio/avcb/", "condominio/limpeza-caixa-dagua/", "condominio/para-raios-spda/"],
    },
    {
        "caminho": "condominio/avcb/",
        "app": "carteira",
        "title": "AVCB do condomínio: o que é, validade e como renovar | MF Agentes",
        "h1": "AVCB do condomínio: o que é, validade e como renovar",
        "descricao": "Entenda o AVCB do condomínio: para que serve, onde ver a validade, quais manutenções e laudos são cobrados na vistoria e como se organizar para renovar sem correria.",
        "lead": "O Auto de Vistoria do Corpo de Bombeiros (AVCB) mostra que o prédio cumpre as exigências de segurança contra incêndio. Sem ele em dia, o condomínio pode ser multado e ter dificuldade com o seguro.",
        "secoes": [
            ("O que é o AVCB", [
                "É o documento emitido pelo Corpo de Bombeiros depois de vistoriar a edificação e conferir que os sistemas de segurança contra incêndio estão instalados e funcionando conforme o projeto aprovado. Em alguns estados, edificações menores recebem um certificado simplificado no lugar dele (em São Paulo, por exemplo, o CLCB).",
                "O nome e as regras variam de estado para estado, porque cada Corpo de Bombeiros tem sua própria regulamentação.",
            ]),
            ("Qual é a validade", [
                "A data de validade vem impressa no próprio certificado. No estado de São Paulo, por exemplo, a validade costuma ser maior para prédios residenciais do que para locais de reunião de público. Confira sempre a data no seu documento e as regras do Corpo de Bombeiros do seu estado.",
                "Não deixe para a última hora: a renovação pode exigir reparos, novos laudos e uma nova vistoria. Comece a organizar com alguns meses de antecedência.",
            ]),
            ("O que costuma ser verificado", [
                "Extintores, hidrantes e mangueiras, iluminação de emergência, sinalização e rotas de fuga livres, alarme e detecção, portas corta-fogo, bombas de incêndio e, quando exigido, para-raios (SPDA) e instalações elétricas das áreas comuns, com os atestados e ARTs dos responsáveis técnicos.",
                "Também é comum ser pedido o projeto técnico de segurança contra incêndio aprovado. Prédios antigos às vezes não têm esse projeto e precisam regularizar antes.",
            ]),
            ("Como se organizar para a renovação", [
                "Mantenha em dia as manutenções periódicas e guarde os comprovantes de cada uma ao longo dos anos. Assim, na hora da renovação, os documentos já estão prontos e não há surpresa.",
                "Anote a validade do AVCB e de cada laudo em uma lista única. Se você administra vários prédios, um painel com alertas evita que um vencimento passe despercebido.",
            ]),
        ],
        "faq": [
            ("O que acontece se o AVCB vencer?", "O condomínio fica sujeito a multa e a outras sanções previstas na regulamentação do estado, e pode ter dificuldade para receber o seguro em caso de incêndio. Em caso de tragédia, o síndico pode ser responsabilizado."),
            ("O Corpo de Bombeiros faz vistoria sem aviso?", "Pode fazer. No estado de São Paulo, o regulamento de segurança contra incêndio permite a fiscalização das edificações. Vistorias também costumam acontecer após denúncias."),
            ("Quem faz o pedido de renovação?", "Normalmente uma empresa ou profissional habilitado contratado pelo condomínio, que reúne os laudos, acompanha a vistoria e cuida das exigências."),
        ],
        "relacionados": ["condominio/manutencoes-obrigatorias/", "condominio/para-raios-spda/", "condominio/limpeza-caixa-dagua/"],
    },
    {
        "caminho": "condominio/limpeza-caixa-dagua/",
        "app": "carteira",
        "title": "Limpeza da caixa d'água do condomínio: de quanto em quanto tempo? | MF Agentes",
        "h1": "Limpeza da caixa d'água do condomínio: de quanto em quanto tempo",
        "descricao": "Com que frequência limpar a caixa d'água do condomínio, quando antecipar a limpeza, o que pedir para a empresa contratada e como registrar o serviço.",
        "lead": "A caixa d'água abastece todos os apartamentos, então qualquer descuido afeta todo mundo. A recomendação mais comum é limpar e desinfetar a cada seis meses, e pelo menos uma vez por ano.",
        "secoes": [
            ("Frequência recomendada", [
                "Órgãos de saúde, como a Secretaria da Saúde do Rio Grande do Sul, orientam limpar e desinfetar o reservatório no mínimo uma vez por ano, com recomendação de fazer a cada seis meses. Algumas cidades e estados têm regras próprias, então confira a legislação do seu município.",
                "Antecipe a limpeza se a água mudar de cor, cheiro ou gosto, se algo ou algum animal entrar no reservatório, ou depois de obras e reparos na rede.",
            ]),
            ("Contrate uma empresa especializada", [
                "Em condomínios, o mais seguro é contratar uma empresa especializada e licenciada. Peça o certificado ou comprovante do serviço, com a data, os reservatórios limpos e os produtos usados, e guarde junto com os outros documentos do prédio.",
                "Muitos condomínios também fazem a análise de potabilidade da água em laboratório depois da limpeza, para comprovar a qualidade.",
            ]),
            ("Como avisar os moradores", [
                "Comunique a data com antecedência, porque o abastecimento é interrompido por algumas horas. Depois do serviço, registre a data da próxima limpeza no calendário de manutenções.",
            ]),
        ],
        "faq": [
            ("Existe lei que obriga a limpeza semestral?", "Depende do lugar. Há municípios e estados com regras próprias, e a vigilância sanitária local pode ter exigências. A frequência semestral é a recomendação mais comum dos órgãos de saúde."),
            ("O zelador pode fazer a limpeza?", "Em casas, a limpeza pode ser feita pelo morador seguindo as orientações sanitárias. Em condomínios, o recomendado é contratar empresa especializada, que entrega o comprovante do serviço."),
            ("Preciso guardar o certificado?", "Sim. Ele comprova que o serviço foi feito e ajuda na prestação de contas aos condôminos e em eventual fiscalização."),
        ],
        "relacionados": ["condominio/manutencoes-obrigatorias/", "condominio/avcb/", "condominio/para-raios-spda/"],
    },
    {
        "caminho": "condominio/para-raios-spda/",
        "app": "carteira",
        "title": "Para-raios (SPDA) do condomínio: inspeção, laudo e prazos | MF Agentes",
        "h1": "Para-raios (SPDA) do condomínio: inspeção, laudo e prazos",
        "descricao": "Com que frequência inspecionar o para-raios (SPDA) do condomínio segundo a NBR 5419, o que entra no laudo e por que ele é cobrado na vistoria do AVCB.",
        "lead": "O Sistema de Proteção contra Descargas Atmosféricas (SPDA), conhecido como para-raios, protege o prédio e as pessoas. Ele precisa de inspeção periódica e de laudo assinado por profissional habilitado.",
        "secoes": [
            ("Com que frequência inspecionar", [
                "A norma ABNT NBR 5419 (edição de 2015) prevê inspeção completa a cada três anos para a maioria das estruturas, e a cada ano para estruturas em áreas de corrosão atmosférica severa, como regiões litorâneas, entre outros casos.",
                "Além da inspeção completa, vale fazer verificações visuais entre uma e outra, principalmente depois de tempestades fortes, obras na cobertura ou instalação de antenas.",
            ]),
            ("O que entra no laudo", [
                "Medição da resistência de aterramento, estado das hastes, captores, cabos e conexões, fixações e isoladores, continuidade das descidas e, quando houver, a luz piloto do mastro.",
                "O laudo deve dizer se o sistema está conforme a norma. Se forem necessários reparos, o documento aponta o que corrigir antes de atestar a conformidade.",
            ]),
            ("Quem assina", [
                "O laudo deve ser feito por profissional habilitado, normalmente engenheiro eletricista, com ART (Anotação de Responsabilidade Técnica). Esse documento costuma ser pedido na vistoria do AVCB.",
            ]),
        ],
        "faq": [
            ("Meu prédio precisa de para-raios?", "Depende da altura, da área e do uso da edificação, conforme a análise de risco da NBR 5419 e as exigências do Corpo de Bombeiros do seu estado. A maioria dos prédios residenciais com vários andares tem."),
            ("O laudo do SPDA vale por quanto tempo?", "Ele reflete a situação no dia da inspeção. A próxima inspeção completa segue a periodicidade da norma, normalmente de três anos, ou um ano em áreas de corrosão severa."),
            ("Posso trocar só o que estiver danificado?", "Sim, mas o reparo deve seguir o projeto e a norma, e o ideal é que o mesmo profissional ateste o sistema depois."),
        ],
        "relacionados": ["condominio/manutencoes-obrigatorias/", "condominio/avcb/", "condominio/limpeza-caixa-dagua/"],
    },
    # ---------------- Estoque Inteligente ----------------
    {
        "caminho": "estoque/controle-de-estoque-restaurante/",
        "app": "estoque",
        "title": "Controle de estoque para restaurante: como fazer sem planilha | MF Agentes",
        "h1": "Controle de estoque para restaurante, sem planilha",
        "descricao": "Como controlar o estoque do restaurante: o que contar, com que frequência, como evitar desperdício e falta de insumo, e como montar a lista de compras com o custo estimado.",
        "lead": "No restaurante, estoque mal controlado vira desperdício, falta de ingrediente na hora do pico e compra de urgência mais cara. Um controle simples, feito todo dia, resolve a maior parte disso.",
        "secoes": [
            ("O que controlar", [
                "Comece pelos insumos que mais pesam no custo e pelos que estragam rápido: carnes, laticínios, hortifrúti e bebidas. Depois inclua os secos, descartáveis e produtos de limpeza.",
                "Para cada item, defina um estoque mínimo: a quantidade abaixo da qual você precisa comprar para não faltar até a próxima entrega.",
            ]),
            ("Rotina que funciona", [
                "Dê entrada em tudo que chega, a partir da nota fiscal. Confira as quantidades e a validade no recebimento.",
                "Use o primeiro que vence primeiro (PVPS): o mais antigo vai para a frente da prateleira.",
                "Faça uma contagem rápida dos itens críticos todo dia e uma contagem completa toda semana. A diferença entre o que deveria ter e o que tem mostra perdas e desperdício.",
            ]),
            ("Compras na medida certa", [
                "Com o mínimo de cada item e a contagem em dia, a lista de compras sai quase pronta: é só repor o que ficou abaixo do mínimo. Assim você compra menos por impulso e evita a compra de urgência.",
            ]),
        ],
        "faq": [
            ("Com que frequência contar o estoque do restaurante?", "Os itens críticos e perecíveis, todo dia ou a cada turno. O estoque completo, uma vez por semana. Itens de giro lento podem ser contados uma vez por mês."),
            ("Planilha resolve?", "Resolve no começo, mas depende de alguém digitar tudo. O que costuma falhar é a atualização diária, e aí a planilha deixa de refletir a realidade."),
            ("Como reduzir o desperdício?", "Receba conferindo a validade, organize por PVPS, defina mínimos realistas e acompanhe a diferença entre o estoque esperado e o contado."),
        ],
        "relacionados": ["estoque/controle-de-estoque-bar/", "estoque/controle-de-estoque-salao-de-beleza/"],
    },
    {
        "caminho": "estoque/controle-de-estoque-bar/",
        "app": "estoque",
        "title": "Controle de estoque para bar: bebidas, perdas e compras | MF Agentes",
        "h1": "Controle de estoque para bar: bebidas, perdas e compras",
        "descricao": "Como controlar o estoque do bar: contagem de bebidas, estoque mínimo, perdas e quebras, e como montar a lista de compras certa para o fim de semana.",
        "lead": "No bar, a bebida é o maior custo e a maior fonte de perda. Saber quanto tem de cada uma, antes da sexta-feira, faz diferença no caixa e evita dizer \"acabou\" para o cliente.",
        "secoes": [
            ("Separe o que mais importa", [
                "Cervejas, destilados, refrigerantes, gelo e insumos de drinks são os itens que mais giram e mais custam. Comece o controle por eles.",
                "Defina um estoque mínimo por item, pensando no movimento do fim de semana e no prazo de entrega do fornecedor.",
            ]),
            ("Rotina de contagem", [
                "Conte as bebidas no fechamento ou antes de abrir, sempre no mesmo momento. Garrafas abertas de destilados podem ser contadas em frações (meia, um quarto).",
                "Compare o que saiu do estoque com o que foi vendido. A diferença mostra quebra, cortesia não registrada ou desvio.",
                "Dê entrada nas compras pela nota fiscal, assim que a mercadoria chegar.",
            ]),
            ("Compre antes do pico", [
                "Com a contagem em dia, a lista de compras para o fim de semana sai do que está abaixo do mínimo. Você evita tanto a falta quanto o dinheiro parado em bebida que não gira.",
            ]),
        ],
        "faq": [
            ("Como evitar perdas no bar?", "Conte sempre no mesmo horário, registre quebras e cortesias, e compare o que saiu do estoque com o que foi vendido."),
            ("Preciso contar todo dia?", "Os itens de maior giro e valor, sim, ou pelo menos antes e depois de cada fim de semana. O restante pode ser semanal."),
            ("Dá para controlar pelo celular?", "Dá. O ideal é um app em que você só confirma o que a câmera leu, sem digitar item por item."),
        ],
        "relacionados": ["estoque/controle-de-estoque-restaurante/", "estoque/controle-de-estoque-salao-de-beleza/"],
    },
    {
        "caminho": "estoque/controle-de-estoque-salao-de-beleza/",
        "app": "estoque",
        "title": "Controle de estoque para salão de beleza: produtos e reposição | MF Agentes",
        "h1": "Controle de estoque para salão de beleza",
        "descricao": "Como controlar o estoque do salão de beleza: produtos de uso nos serviços e de revenda, estoque mínimo, validade e lista de reposição com o custo estimado.",
        "lead": "No salão, faltar a tinta, o tratamento ou o produto da escova no meio do atendimento atrapalha o dia inteiro. E produto vencido é dinheiro jogado fora.",
        "secoes": [
            ("Separe uso e revenda", [
                "Os produtos usados nos serviços (coloração, oxidante, tratamentos, descartáveis) e os produtos de revenda têm giros diferentes. Controle os dois, mas com mínimos próprios.",
                "Nas colorações, controle por tom ou número, que é onde a falta mais aparece.",
            ]),
            ("Rotina simples", [
                "Dê entrada nas compras pela nota fiscal e confira a validade de cada lote.",
                "Use primeiro o que vence primeiro e faça uma contagem semanal dos produtos mais usados.",
                "Defina o estoque mínimo pensando na agenda da semana e no prazo do distribuidor.",
            ]),
            ("Reposição sem esquecer nada", [
                "Com a contagem em dia, a lista de reposição mostra só o que está abaixo do mínimo, com o custo estimado. Fica mais fácil negociar com o distribuidor e não comprar em excesso.",
            ]),
        ],
        "faq": [
            ("Como controlar o estoque de tintas por tom?", "Cadastre cada tom como um item separado, com seu estoque mínimo. Assim a lista de reposição mostra exatamente os números que estão acabando."),
            ("Com que frequência contar?", "Os produtos mais usados nos serviços, toda semana. Revenda e itens de giro lento, uma vez por mês."),
            ("Como evitar produto vencido?", "Confira a validade no recebimento, organize para usar primeiro o que vence antes e acompanhe os itens parados há muito tempo."),
        ],
        "relacionados": ["estoque/controle-de-estoque-restaurante/", "estoque/controle-de-estoque-bar/"],
    },
]

TITULO_POR_CAMINHO = {p["caminho"]: p["h1"] for p in PAGINAS}

CSS = """
  :root { --paper:#F3F5F1; --paper-2:#E7ECE4; --ink:#1D2721; --ink-soft:#4A564E; --sage:#7E9C85; --sage-deep:#2E4236; --sage-light:#C9D8C5; --line:#D3DBD0; --white:#FFFFFF; }
  * { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }
  body { margin:0; background:var(--paper); color:var(--ink); font-family:"Schibsted Grotesk", system-ui, -apple-system, "Segoe UI", sans-serif; font-size:1.0625rem; line-height:1.65; -webkit-font-smoothing:antialiased; }
  a { color: var(--sage-deep); }
  :focus-visible { outline:3px solid var(--sage); outline-offset:3px; border-radius:6px; }
  .wrap { max-width:760px; margin:0 auto; padding:0 24px; }
  header { padding:22px 0; }
  header .wrap { display:flex; align-items:center; justify-content:space-between; gap:16px; }
  .brand { display:flex; align-items:center; gap:10px; text-decoration:none; color:var(--ink); font-weight:800; font-size:1.15rem; letter-spacing:-0.02em; }
  .brand svg { width:28px; height:28px; }
  .back { font-weight:600; font-size:0.95rem; text-decoration:none; border-bottom:2px solid var(--sage-light); padding:6px 0; }
  .crumbs { font-size:0.88rem; color:var(--ink-soft); margin:20px 0 10px; }
  .crumbs a { color:var(--ink-soft); }
  h1 { font-size:clamp(1.9rem, 5.5vw, 2.7rem); line-height:1.08; letter-spacing:-0.03em; font-weight:800; margin:0 0 16px; }
  .lead { color:var(--ink-soft); font-size:1.14rem; margin:0 0 10px; }
  .upd { font-size:0.86rem; color:var(--ink-soft); margin:0 0 28px; }
  h2 { font-size:1.4rem; letter-spacing:-0.02em; margin:36px 0 10px; }
  p { margin:0 0 14px; }
  .table-wrap { overflow-x:auto; background:var(--white); border:1px solid var(--line); border-radius:16px; margin:8px 0 10px; }
  table { border-collapse:collapse; width:100%; font-size:0.96rem; }
  th, td { text-align:left; padding:11px 14px; border-bottom:1px solid var(--line); vertical-align:top; }
  th { background:var(--paper-2); font-weight:700; }
  tr:last-child td { border-bottom:0; }
  td:first-child { font-weight:600; }
  .nota { font-size:0.9rem; color:var(--ink-soft); }
  .cta { background:var(--sage-deep); color:var(--white); border-radius:22px; padding:26px 24px; margin:40px 0 8px; }
  .cta h2 { color:var(--white); margin:0 0 8px; font-size:1.35rem; }
  .cta p { color:var(--sage-light); margin:0 0 18px; }
  .btn { display:inline-flex; align-items:center; justify-content:center; font:inherit; font-weight:700; text-decoration:none; padding:13px 24px; border-radius:999px; background:var(--sage-light); color:var(--ink); }
  .btn:hover { background:var(--white); }
  details { background:var(--white); border:1px solid var(--line); border-radius:16px; margin:0 0 10px; }
  summary { list-style:none; cursor:pointer; padding:16px 18px; font-weight:700; display:flex; justify-content:space-between; gap:12px; }
  summary::-webkit-details-marker { display:none; }
  summary::after { content:"+"; font-size:1.4rem; font-weight:500; color:var(--sage-deep); line-height:1; }
  details[open] summary::after { content:"–"; }
  details p { padding:0 18px 16px; margin:0; color:var(--ink-soft); }
  .aviso { background:var(--white); border:1px solid var(--line); border-left:5px solid var(--sage); border-radius:14px; padding:14px 16px; font-size:0.92rem; color:var(--ink-soft); margin:28px 0 0; }
  .rel ul { list-style:none; padding:0; margin:0; display:grid; gap:10px; }
  .rel a { display:block; background:var(--white); border:1px solid var(--line); border-radius:14px; padding:14px 16px; font-weight:600; text-decoration:none; color:var(--ink); }
  .rel a:hover { border-color:var(--sage); }
  footer { margin-top:56px; border-top:1px solid var(--line); padding:24px 0 40px; font-size:0.9rem; color:var(--ink-soft); }
  footer .wrap { display:flex; flex-wrap:wrap; gap:8px 18px; }
  footer button { font:inherit; background:none; border:0; padding:0; color:var(--sage-deep); text-decoration:underline; cursor:pointer; }
  @media (max-width:520px) { .wrap { padding:0 16px; } th, td { padding:10px; } }
"""

ICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4236'/%3E%3Cpath d='M9 16.5l4.5 4.5L23 11.5' fill='none' stroke='%23C9D8C5' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"

e = html.escape


def paragrafos(lista):
    return "\n".join(f"  <p>{e(t)}</p>" for t in lista)


def secoes(lista):
    return "\n".join(f"  <h2>{e(t)}</h2>\n{paragrafos(ps)}" for t, ps in lista)


def render(p):
    url = f"{SITE}/{p['caminho']}"
    cta = CTA[p["app"]]
    area = "Condomínio" if p["app"] == "carteira" else "Estoque"
    area_href = "/#app-carteirapredial" if p["app"] == "carteira" else "/#app-estoque"
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": p["h1"],
                "description": p["descricao"],
                "url": url,
                "inLanguage": "pt-BR",
                "dateModified": HOJE,
                "author": {"@type": "Organization", "name": "MF Agentes", "url": SITE},
                "publisher": {"@type": "Organization", "name": "MF Agentes", "url": SITE},
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in p["faq"]
                ],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "MF Agentes", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url},
                ],
            },
        ],
    }
    tabela = ""
    if p.get("tabela"):
        t = p["tabela"]
        cab = "".join(f"<th>{e(c)}</th>" for c in t["colunas"])
        linhas = "\n".join("      <tr>" + "".join(f"<td>{e(c)}</td>" for c in l) + "</tr>" for l in t["linhas"])
        tabela = (
            f"  <h2>{e(t['titulo'])}</h2>\n  <div class=\"table-wrap\"><table>\n    <thead><tr>{cab}</tr></thead>\n    <tbody>\n{linhas}\n    </tbody>\n  </table></div>\n"
            f"  <p class=\"nota\">{e(t['nota'])}</p>\n"
        )
    faq = "\n".join(f"  <details><summary>{e(q)}</summary><p>{e(r)}</p></details>" for q, r in p["faq"])
    rel = "\n".join(f"      <li><a href=\"/{c}\">{e(TITULO_POR_CAMINHO[c])}</a></li>" for c in p["relacionados"])
    aviso = f'  <p class="aviso">{e(AVISO_LEGAL)}</p>\n' if p["app"] == "carteira" else ""
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['descricao'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(p['h1'])}">
<meta property="og:description" content="{e(p['descricao'])}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#2E4236">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script src="/analytics.js" defer></script>
</head>
<body>
<header>
  <div class="wrap">
    <a class="brand" href="/" aria-label="MF Agentes, página inicial">
      <svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#2E4236"/><path d="M9 16.5l4.5 4.5L23 11.5" fill="none" stroke="#C9D8C5" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      MF Agentes
    </a>
    <a class="back" href="/">Voltar ao site</a>
  </div>
</header>
<main class="wrap">
<article>
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › <a href="{area_href}">{area}</a></nav>
  <h1>{e(p['h1'])}</h1>
  <p class="lead">{e(p['lead'])}</p>
  <p class="upd">{ATUALIZADO} · MF Agentes</p>
{secoes(p['secoes'])}
{tabela}{secoes(p.get('secoes_depois', []))}
  <section class="cta">
    <h2>{e(cta['titulo'])}</h2>
    <p>{e(cta['texto'])}</p>
    <a class="btn" href="{e(cta['href'])}" target="_blank" rel="noopener">{e(cta['botao'])}</a>
  </section>
  <h2>Perguntas frequentes</h2>
{faq}
{aviso}  <section class="rel">
    <h2>Leia também</h2>
    <ul>
{rel}
    </ul>
  </section>
</article>
</main>
<footer>
  <div class="wrap">
    <span>© 2026 MF Agentes. Atendimento 100% remoto para todo o Brasil.</span>
    <span>Contato: <a href="mailto:suporte@mfagentes.com.br">suporte@mfagentes.com.br</a></span>
    <button type="button" onclick="window.mfCookiePreferences && window.mfCookiePreferences()">Preferências de cookies</button>
  </div>
</footer>
</body>
</html>
"""


def main():
    for p in PAGINAS:
        os.makedirs(p["caminho"], exist_ok=True)
        with open(os.path.join(p["caminho"], "index.html"), "w", encoding="utf-8") as f:
            f.write(render(p))
    urls = ["", "instalar/"] + [p["caminho"] for p in PAGINAS]
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f"  <url><loc>{SITE}/{u}</loc><lastmod>{HOJE}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /_tools/\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(PAGINAS)} páginas geradas")


if __name__ == "__main__":
    main()
