# Exercicio gerando PDF com formato de lista
from reportlab.pdfgen import canvas


def GeneratePDF(lista):
    try:
        nome = input('Digite o seu nome')
        idade = input('Digite a sua idade')
        nome_pdf = input('Informe aqui o nome que quer no seu PDF')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        while idade:
            if idade == 0:
                break
            print('Erro ao gerar o seu pdf')
            for nome_pdf, idade in lista():
                x -= 20
    pdf.drawString(247, x, '{},{}'.format(nome, idade))
    pdf.setTitle(nome_pdf)
    pdf.setFont('Helvertica', 14)
    pdf.drawString(245, 750, 'Lista de Clientes')
    pdf.setFont('Helvertica-Bold', 12)
    pdf.drawString(245, 724, 'Nome e idade')
    pdf.save()
    print('{}.pdf foi criado com sucesso, parabens.'.format(nome_pdf))
    except:
    print('Infelizmente o seu pdf não consegui ser criado')


GeneratePDF(Lista=)   