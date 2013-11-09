$( '#search_button' ).click(function(e) {
    e.preventDefault();
    $("#contenido").html("");
    $.getJSON( "proyectos_data.json", function( data ) {
        $.each(data, function(i, v) {
        
        var out = '';
        if( v.titulo.search(new RegExp(/propone/i)) != -1 ) {
            out += '\n<p>' + v.titulo;
            out += ' <span class="glyphicon glyphicon-cloud-download"></span>';
            out += ' <a href="' + v.pdf_url + '">PDF</a>';
            out += ' <span class="glyphicon glyphicon-link"></span>';
            out += ' <a href="' + v.link_to_pdf + '">Expediente</a>';
            out += '</p>'
            console.log(v);
            console.log(v.titulo);
            console.log(out);
            $("#contenido").append(out);
        }
    });
});
});
