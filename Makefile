REPO := agenticworkflow/chatgpt-ui
VERSION := v240812

build:
	docker build \
	-t $(REPO):$(VERSION) \
	.

