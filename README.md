# Ymerflow-plugin-processes

Image/artifact-building YmerFlow process types that depend on the **plugin SDK**
(`Ymerflow-plugin-sdk` / `ymerflow_plugin_build`):

- **`build_frontend_plugin`** — builds a YmerFlow frontend plugin (an npm source package) into a
  Module-Federation remote and writes it as a directory dataset (`application/x-mf-remote`),
  auto-registering it as a Plugin/PluginVersion on completion.

Kept separate from `Ymerflow-process-sdk` so the runner SDK stays free of the plugin SDK dependency.

Installed via `pip install "git+https://github.com/YmerFlow/Ymerflow-plugin-processes.git"`.

## Testing

`tests/fixtures/cluster-test-widget/` is a pure-frontend test plugin. CI (`.github/workflows/ci.yml`)
`npm pack`s it and runs the real `ymerflow_plugin_build` build routine, asserting a `remoteEntry.js`
is produced. This is the smoke-test that used to run at base-runner image-build time; production
`build_frontend_plugin` resolves real plugins from the admin-populated npm source PVC, not this
fixture.
