import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), 'utf8');

test('the marketing site is an Astro site with four substantive routes', async () => {
  const packageJson = JSON.parse(await read('package.json'));
  assert.ok(packageJson.dependencies.astro, 'Astro must remain the site framework');
  assert.equal(packageJson.dependencies.jekyll, undefined);
  assert.equal(packageJson.dependencies.hugo, undefined);

  const routes = await Promise.all([
    'src/pages/index.astro',
    'src/pages/workflow/index.astro',
    'src/pages/platform/index.astro',
    'src/pages/trust/index.astro',
  ].map(read));

  for (const route of routes) {
    assert.match(route, /<Layout/);
  }
});

test('shared navigation exposes sticky, responsive access paths', async () => {
  const [header, footer, styles] = await Promise.all([
    read('src/components/Header.astro'),
    read('src/components/Footer.astro'),
    read('src/styles/global.css'),
  ]);

  assert.match(header, /class="site-header"/);
  assert.match(header, /class="mobile-nav"/);
  assert.match(header, /https:\/\/user\.chapter-publishing\.github\.io/);
  assert.match(header, /https:\/\/auth\.chapter-publishing\.github\.io/);
  assert.match(footer, /<footer/);
  assert.match(styles, /position:\s*sticky/);
  assert.match(styles, /@media\s*\(max-width:/);
});

test('Pages publishes the built Astro artifact', async () => {
  const workflow = await read('.github/workflows/pages.yml');
  assert.match(workflow, /npm run build/);
  assert.match(workflow, /path:\s*dist/);
  assert.doesNotMatch(workflow, /path:\s*\.\s*$/m);
});
