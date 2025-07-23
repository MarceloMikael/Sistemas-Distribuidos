import axios from 'axios';

const baseUrl = 'http://localhost:8080/residencial';

const imovel = {
    id: '101',
    endereco: 'Rua das Flores, 45',
    preco: 300000,
    proprietario: {
        nome: 'Carlos Silva',
        cpf: '12345678901'
    }
};

const comprador = {
    nome: 'Ana Maria',
    cpf: '98765432100'
};

async function executar() {
    try {
        await axios.post(`${baseUrl}/imoveis`, imovel);
        console.log('Imóvel cadastrado');

        const disp = await axios.get(`${baseUrl}/imoveis`);
        console.log('Disponíveis:', disp.data);

        await axios.post(`${baseUrl}/imoveis/${imovel.id}/vender`, comprador);
        console.log('Imóvel vendido');

        const vendas = await axios.get(`${baseUrl}/vendas`);
        console.log('Vendas:', vendas.data);
    } catch (err) {
        console.error('Erro:', err.response?.data || err.message);
    }
}

executar();
