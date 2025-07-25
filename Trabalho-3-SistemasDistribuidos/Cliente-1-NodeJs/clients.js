import axios from 'axios';

// const baseUrl = 'http://localhost:8080/residencial';
const baseUrl = 'http://172.25.164.135:8080/residencial';
const imovel = {
    id: '102',
    endereco: 'Rua dos Santos, 42',
    preco: 150000,
    proprietario: {
        nome: 'João Maria',
        cpf: '12345678901'
    }
};

const comprador = {
    nome: 'Maria José',
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
