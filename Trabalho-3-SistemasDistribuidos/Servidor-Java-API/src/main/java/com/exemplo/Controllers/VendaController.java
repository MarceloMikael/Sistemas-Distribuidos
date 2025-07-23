package com.exemplo.Controllers;

import com.exemplo.model.Cliente;
import com.exemplo.model.Imovel;
import com.exemplo.Services.VendaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/{tipo}")
public class VendaController {

    @Autowired
    private VendaService vendaService;

    @PostMapping("/imoveis")
    public void cadastrarImovel(@RequestBody Imovel imovel) {
        vendaService.cadastrarImovel(imovel);
    }

    @PostMapping("/imoveis/{id}/vender")
    public boolean venderImovel(@PathVariable String id, @RequestBody Cliente cliente) {
        return vendaService.venderImovel(id, cliente);
    }

    @GetMapping("/imoveis")
    public List<Imovel> listarImoveis() {
        return vendaService.getImovels();
    }

    @GetMapping("/vendas")
    public List<Imovel> listarVendas() {
        return vendaService.listarVendas();
    }
}