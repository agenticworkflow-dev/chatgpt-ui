REPO := agenticworkflow/chatgpt-ui
VERSION := v240924

build:
	docker build \
	-t $(REPO):$(VERSION) \
	.

