# Para rodar o modulo myapp, execute dentro do terminal na pasta do chapter8
```
python3 -m myapp 
```
Tendo como resultado
```
Aplicação iniciada!
{'x': 1, 'y': 2}

```


# Para gerar um pacote para distribuir executar na pasta do chapter8
```
python setup.py sdist
```

## Para instalar, entre na pasta criada chamada dist
```python3 -m pip install myapp-1.0.tar.gz```


