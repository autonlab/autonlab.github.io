FROM python:3-slim AS basebuild

RUN pip install --target=/wf-support bibtexparser

# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=basebuild /wf-support /wf-support
ENV PYTHONPATH /wf-support
CMD ["/python_scripts/bt2json.py"]