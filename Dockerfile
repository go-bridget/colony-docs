FROM squidfunk/mkdocs-material

RUN	apk --no-cache add graphviz msttcorefonts-installer fontconfig && \
	update-ms-fonts && \
	fc-cache -f && \
	pip install --no-cache-dir mkdocs-diagrams