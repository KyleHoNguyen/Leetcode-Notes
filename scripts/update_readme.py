from pathlib import Path
import random
import re
import subprocess
from collections import defaultdict

random.seed(0)

def get_last_modified_date(fpath, timestamp=False):
    fmt = "%as"
    if timestamp:
        fmt = "%at"
    cmd = f"git log --pretty=format:{fmt}__%ae --".split()
    cmd += [str(fpath)]
    response = subprocess.run(cmd, capture_output=True)
    commits = response.stdout.decode()
    commits = commits.split()
    for c in commits:
        outv, author_email = c.split('__')
        if author_email != 'action@github.com':
            break
    return outv

def badges2kv(text):
    outv = badges2kv_labels(text)
    if not outv:
        outv = badges2kv_regex(text)
    return outv

def badges2kv_labels(text):
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    lines = [line for line in lines if not line.startswith('#')]
    if lines[0].startswith('labels:'):
        labels = lines[0].replace('labels:', '').strip().split(',')
        return [('tag', label.strip()) for label in labels]

def badges2kv_regex(text):
    testpat = r'\/([a-zA-Z]+-[a-zA-Z_]+-[a-zA-Z]+)'
    badges = re.findall(testpat, text)
    return [(b.split('-')[0], b.split('-')[1]) for b in badges]

def get_time_completed(text):
    """Extracts the 'Time Completed:' value from the document."""
    time_pat = r'Time Completed:\s*(\S+)'
    match = re.search(time_pat, text)
    return match.group(1) if match else "N/A"

def make_badge(label, prefix='tag', color='lightgrey', root='.'):
    return f"[![](https://img.shields.io/badge/{prefix}-{label}-{color})]({root}/tags/{label}.md)"

def random_hex_color():
    r = lambda: random.randint(0, 255)
    return f"{r():x}{r():x}{r():x}"

md_files = Path('.').glob('*.md')
TOC = []
unq_tags = defaultdict(list)

for fpath in list(md_files):
    if fpath.name == 'README.md':
        continue
    with open(fpath) as f:
        header = f.readline()
        if header.startswith('# '):
            text = f.read()
            badge_meta = badges2kv(text)
            d_ = {'fpath': fpath}
            d_['problem_name'] = header[2:].strip()
            d_['date_completed'] = get_last_modified_date(fpath)
            d_['time_completed'] = get_time_completed(text)
            d_['tags'] = [v for k, v in badge_meta if k == 'tag']
            d_['tags'].sort()
            for tag in d_['tags']:
                unq_tags[tag].append(d_)
            TOC.append(d_)

tag_badges_map = {tag_name: make_badge(label=tag_name, color=random_hex_color()) for tag_name in unq_tags}

def make_badges(unq_tags, sep=' '):
    return sep.join([tag_badges_map[tag] for tag in unq_tags])

TOC = sorted(TOC, key=lambda x: x['date_completed'])[::-1]

header = "|Date Completed|Problem Name|Time Completed  (minutes)|Tags\n|:---|:---|---:|:---|\n"
recs = [f"|{d['date_completed']}|[{d['problem_name']}]({ Path('.')/d['fpath'] })|{d['time_completed']}|{make_badges(d['tags'])}|" for d in TOC]
toc_str = header + '\n'.join(recs)

readme = None
if Path('README.stub').exists():
    with open('README.stub') as f:
        readme_stub = f.read()
    readme = readme_stub.replace('{TOC}', toc_str)
    readme = readme.replace('{tags}', make_badges(unq_tags))
    readme = readme.strip()
if not readme:
    with open('empty.stub') as f:
        readme = f.read()

with open('README.md', 'w') as f:
    f.write(readme)

# Adjust tag badges map for tag-specific pages
tag_badges_map = {tag_name: make_badge(label=tag_name, color=random_hex_color(), root='..') for tag_name in unq_tags}
def make_badges(unq_tags, sep=' '):
    return sep.join([tag_badges_map[tag] for tag in unq_tags])

Path("tags").mkdir(exist_ok=True)
for tag, pages in unq_tags.items():
    pages = sorted(pages, key=lambda x: x['date_completed'])[::-1]
    recs = [f"|{d['date_completed']}|[{d['problem_name']}]({ Path('..')/d['fpath'] })|{d['time_completed']}|{make_badges(d['tags'])}|" for d in pages]
    with open(f"tags/{tag}.md", 'w') as f:
        page_str = f"# Pages tagged `{tag}`\n\n"
        page_str += header + '\n'.join(recs)
        f.write(page_str)
