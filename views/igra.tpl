% import model

<!DOCTYPE html>
<html>
<title> Vislice </title>
<body>

  <h1>Vislice ID: {{id_igre}}</h1>



   <blockquote>
   <b>  
    {{igra.pravilni_del_gesla()}}
   </b>
    

  <blockquote>
  
    Nepravilni poskusi: {{igra.nepravilni_ugibi()}}
  

  </blockquote>
  <blockquote>
      Vsi poskusi: {{igra.stevilo_napak()}} /{{model.STEVILO_DOVOLJENIH_NAPAK}}
    </blockquote>

  <blockquote>
    
  
    % napake = len(igra.napacne_crke())
    % ime_slike = 'img/' + str(napake) + '.jpg'
  <img src={{ime_slike}} alt="Obesanje">
</blockquote>
% if poskus == model.ZMAGA:  
<form action="/igra/" method="post">
  <button type="submit">Nova igra</button>
</form>
!!!ZMAGAL SI!!!
% elif poskus == model.PORAZ:
<form action="/igra/" method="post">
  <button type="submit">Nova igra</button>
</form>
Žal ti ni uspelo, rešitev je {{igra.geslo}}.

  
  % else:
  <form action="/igra/{{id_igre}}" method="POST">
  <input type="text" name="poskus" placeholder="Tu notri napiši eno črko">
  <input type="submit" value="Ugibaj">
  </form>
  % end
</body>

</html>