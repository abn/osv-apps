CFLAGS = -fPIC -shared
LDFLAGS = -fPIC -shared
BIRD_VERSION = 1.4.5
BIRD_CONFIG_OPTS= --disable-client -host x86_64-unknown-linux-gnu

.PHONY: module
module: bird.so
	cp -vf bird/bird bird.so

bird.so: bird
	cd bird && ./configure $(BIRD_CONFIG_OPTS) CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"
	cd bird && make -j4

bird:
	[[ ! -d bird ]] && ./GET ${BIRD_VERSION}
	ln -sf bird-${BIRD_VERSION} bird

clean:
	rm -rf bird bird-*/ *.manifest *.so
