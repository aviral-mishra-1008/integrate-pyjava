package com.integrate_python.ai_java.controller;
import com.integrate_python.ai_java.service.apiService;
import org.apache.coyote.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/generate")
public class apiController {

    @Autowired
    private apiService apiservice;

    @PostMapping("fromText")
    public ResponseEntity<String> queryLLM(@RequestBody String text){
        return apiservice.sendQuery(text);
    }

    @GetMapping("test")
    public  ResponseEntity<String> defaultPage(){
        return new ResponseEntity<String>("Success!", HttpStatus.ACCEPTED);
    }
}
