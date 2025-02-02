package com.integrate_python.ai_java.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class apiService {
    @Autowired
    private RestTemplate restTemplate;
    private final String ml_api = "http://localhost:5000/api/generate-from-prompt";

    public ResponseEntity<String> sendQuery(String prompt) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> requestBody = new HashMap<>();
        requestBody.put("text", prompt);

        HttpEntity<Map<String, String>> request = new HttpEntity<>(requestBody, headers);
        return restTemplate.postForEntity(ml_api, request, String.class);
    }
}
