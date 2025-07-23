package com.exemplo.Services;

import com.exemplo.model.Cliente;
import com.exemplo.model.Imovel;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class VendaService {
    private final Map<String, Imovel> imoveis = new HashMap<>();
    private final List<Imovel> vendas = new ArrayList<>();

    public void cadastrarImovel(Imovel imovel) {
        imoveis.put(imovel.getId(), imovel);
    }

    public boolean venderImovel(String id, Cliente comprador) {
        Imovel imovel = imoveis.get(id);
        if (imovel != null) {
            imovel.setProprietario(comprador);
            vendas.add(imovel);
            imoveis.remove(id);
            return true;
        }
        return false;
    }

    public List<Imovel> getImovels() {
        return new ArrayList<>(imoveis.values());
    }

    public List<Imovel> listarVendas() {
        return vendas;
    }
}