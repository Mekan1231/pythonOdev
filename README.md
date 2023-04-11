#Python decorators
Decorator benºm anladığım kadarıyla c# dilindeki attuributelere benziyor. Pythonda herşey
nesne olarak görüldüği için bir fonksiyon başka bir fonksiyonu parametre olrak alabilir.
tabi bu özelliği decorator kullanmada kullanabiliriz
##Decorator kullanmadan
```python
def printer():
    print("hello world")

def display_info(func):
    def inner():
        print("Exacuting",func.__name__,"function")
        func()
        print("Finished exacution")
    return inner



result= display_info(printer)
result()
```

##Decorator kullanımı
```python
def display_info(func):
    def inner():
        print("Exacuting",func.__name__,"function")
        func()
        print("Finished exacution")
    return inner

@display_info
def printer():
    print("hello world")

printer()
```

#Pytest ile kullanılan decoratorlar

 pytest'te kullanılan decorator'ların tam listesi ve açıklamaları şunlardır:

@pytest.fixture: Test işlevleri tarafından kullanılacak test verilerini veya hazırlık/kaynakları sağlayan bir fonksiyonu işaretlemek için kullanılır. Bu decorator, test fonksiyonunun argüman listesine eklenen bir parametrenin değerini döndürür.

@pytest.mark.parametrize: Test fonksiyonlarının birden fazla kez çağrılmasını sağlamak için kullanılır. Bu decorator, test fonksiyonunun birden fazla kez çalıştırılmasına izin veren bir parametre listesi sağlar.

@pytest.mark.skip: Bir test işlevinin geçici olarak atlanmasını sağlamak için kullanılır.

@pytest.mark.xfail: Bir testin bilinen bir şekilde başarısız olacağını işaretlemek için kullanılır. Bu, testin hala çalışmasına ve çıktıda görünmesine neden olur, ancak başarısız olarak işaretlenir.

@pytest.mark.skipif: Bir test işlevinin belirli bir koşulu karşılamadığı durumlarda atlanmasını sağlamak için kullanılır.

@pytest.mark.timeout: Bir test işlevinin belirli bir sürede tamamlanması gerektiğini işaretlemek için kullanılır.

@pytest.mark.order: Test işlevlerinin çalışma sırasını belirlemek için kullanılır.

@pytest.mark.dependency: Testler arasında bağımlılık oluşturmak için kullanılır.

@pytest.mark.usefixtures: Bir test fonksiyonunun önceden belirlenmiş bir hazırlık işlevi kullanmasını sağlamak için kullanılır.