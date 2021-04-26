FROM python:3.9.4-buster AS builder-backend

COPY . /code/
WORKDIR /code

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
RUN pip wheel . --wheel-dir ./dist/wheels
COPY docker/uwsgi.ini /etc/uwsgi.ini

FROM python:3.9.4-buster
RUN useradd --system --user-group django

# copy all wheel artifacts from the builder-backend image and install them
COPY --from=builder-backend /code/dist/wheels/*.whl /opt/wheels/
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
RUN pip install --no-deps --no-index --find-links /opt/wheels/ /opt/wheels/*.whl

# create public directories
RUN mkdir -p /opt/public/static
RUN mkdir -p /opt/public/media

# copy uwsgi.ini
COPY --from=builder-backend /code/docker/uwsgi.ini /etc/uwsgi.ini

# make django the owner of the web directory
RUN chown -R django /opt/public

EXPOSE 8000
USER django

CMD ["/usr/local/bin/uwsgi", "--ini", "/etc/uwsgi.ini"]