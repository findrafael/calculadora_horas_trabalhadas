from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_horas_trabalhadas(hora_entrada, saida_almoco, volta_almoco, hora_saida):
    entrada_horas, entrada_minutos = map(int, hora_entrada.split(':'))
    saida_almoco_horas, saida_almoco_minutos = map(int, saida_almoco.split(':'))
    volta_almoco_horas, volta_almoco_minutos = map(int, volta_almoco.split(':'))
    saida_horas, saida_minutos = map(int, hora_saida.split(':'))

    horas_trabalhadas_antes_almoco = (saida_almoco_horas - entrada_horas) + (saida_almoco_minutos - entrada_minutos) / 60
    horas_trabalhadas_depois_almoco = (saida_horas - volta_almoco_horas) + (saida_minutos - volta_almoco_minutos) / 60

    total_horas_trabalhadas = horas_trabalhadas_antes_almoco + horas_trabalhadas_depois_almoco

    return total_horas_trabalhadas, total_horas_trabalhadas >= 8

@app.route('/verificar_horas', methods=['POST'])
def verificar_horas():
    data = request.json

    hora_entrada = data.get('hora_entrada')
    saida_almoco = data.get('saida_almoco')
    volta_almoco = data.get('volta_almoco')
    hora_saida = data.get('hora_saida')

    if not hora_entrada or not saida_almoco or not volta_almoco or not hora_saida:
        return jsonify({'message': 'Por favor, forneça todas as informações necessárias'}), 400

    horas_trabalhadas, atende_requisito = calcular_horas_trabalhadas(hora_entrada, saida_almoco, volta_almoco, hora_saida)

    response_data = {
        'message': 'Funcionário trabalhou pelo menos 8 horas' if atende_requisito else 'Funcionário não trabalhou 8 horas',
        'worked_hours': horas_trabalhadas
    }

    return jsonify(response_data), 200 if atende_requisito else 400

if __name__ == '__main__':
    app.run(debug=True)
