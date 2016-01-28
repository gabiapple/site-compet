def thumbnail(link, img, title, desc):
	print """
<div class="col-sm-6">
    <a href="%s" class="thumbnail thumbnail-fix">
        <figure class="cover" style="background-image: url('%s')"></figure>
        <span class="tag">Evento</span>
        <span class="tag tag-2">Minicursos</span>
        <span class="tag tag-3">Minicursos</span>
        <span class="tag tag-4">Minicursos</span>
        <div class="caption">
            <h3>%s</h3>
            <p>%s</p>
        </div>
    </a>
</div>
	""" % (link, img, title, desc)


{
	link: 'url',
	img: 'url',
	tags: [
			'tag1',
			'tag2'
		  ],
	title: 'title',
	description: 'description'
}