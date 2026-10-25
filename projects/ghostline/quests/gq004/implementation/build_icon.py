"""Author and cook Heartbreaker's native monochrome UI glyph."""
import copy
import base64
import json
from pathlib import Path
import subprocess
import sys
from PIL import Image, ImageDraw, ImageOps

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
PROJECT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from toolchain import resolve_tool
from phase_graph import cname


def render_glyph():
    scale = 4
    image = Image.new('RGBA', (256*scale, 256*scale))
    draw = ImageDraw.Draw(image)
    def line(points, width=4, fill=(255,255,255,255)):
        draw.line([(x*scale,y*scale) for x,y in points], fill=fill, width=width*scale, joint='curve')
    # A large broken heart survives the inventory's small raster size.
    points=[]
    curves=[((128,91),(105,55),(66,79),(77,110)),((77,110),(85,133),(108,151),(128,167)),
            ((128,167),(149,151),(171,133),(180,110)),((180,110),(191,79),(151,55),(128,91))]
    for a,b,c,d in curves:
        for i in range(33):
            t=i/32;u=1-t
            points.append(((u*u*u*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t*t*t*d[0])*scale,
                           (u*u*u*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t*t*t*d[1])*scale))
    draw.line(points + [points[0]], fill='white', width=8*scale, joint='curve')
    line([(137,76),(120,106),(137,116),(121,146),(128,168)],10,(0,0,0,0))
    for points in [[(52,112),(65,112)],[(190,112),(204,112)],[(98,164),(98,183),(76,183)]]:line(points,4)
    for x,y in [(52,112),(204,112),(73,183)]:
        draw.ellipse(((x-4)*scale,(y-4)*scale,(x+4)*scale,(y+4)*scale),outline='white',width=3*scale)
    # Velvet's bow, rendered as a silhouette to remain clear under UI tinting.
    for poly in [[(130,176),(149,183),(130,194)],[(170,176),(151,183),(170,194)],
                 [(146,187),(139,202),(148,198),(151,190)],[(154,187),(161,202),(152,198),(149,190)]]:
        draw.polygon([(x*scale,y*scale) for x,y in poly],fill='white')
    draw.ellipse((145*scale,181*scale,155*scale,191*scale),fill='white')
    return image.resize((256,256),Image.Resampling.LANCZOS)


def render():
    """A native 50x65 inventory chip and separate 32x32 HUD glyph at 1080p."""
    atlas = Image.new('RGBA', (256,256))
    scale = 4
    chip = Image.new('RGBA', (100*scale,128*scale))
    d = ImageDraw.Draw(chip)
    def polygon(points, **kwargs):
        d.polygon([(x*scale,y*scale) for x,y in points], **kwargs)
    polygon([(12,9),(83,9),(91,17),(91,113),(82,122),(9,122),(9,17)], fill=(25,33,36), outline=(134,152,154), width=2*scale)
    polygon([(17,24),(81,24),(84,29),(84,109),(78,115),(16,115)], fill=(10,27,32), outline=(70,203,211), width=scale)
    for x in range(19,83,7):
        d.rectangle((x*scale,3*scale,(x+3)*scale,17*scale), fill=(193,159,76))
    for x in range(24,77,9):
        d.rectangle((x*scale,118*scale,(x+3)*scale,125*scale), fill=(137,144,134))
    glyph = render_glyph()
    cyan = Image.new('RGBA',glyph.size,(79,221,228));cyan.putalpha(glyph.getchannel('A'))
    chip.alpha_composite(cyan.resize((78*scale,78*scale),Image.Resampling.LANCZOS),(11*scale,29*scale))
    atlas.alpha_composite(chip.resize((50,65),Image.Resampling.LANCZOS),(0,0))
    atlas.alpha_composite(glyph.resize((32,32),Image.Resampling.LANCZOS),(128,0))
    return atlas


def main():
    raw = PROJECT/'source/raw/mod/gq004/ui'
    archive = PROJECT/'source/archive/mod/gq004/ui'
    work = PROJECT/'generated/gq004-icon'
    for p in (raw,archive,work,work/'readback'):p.mkdir(parents=True,exist_ok=True)
    image=render();image.save(raw/'heartbreaker_1080p.png')
    image.resize((512,512),Image.Resampling.LANCZOS).save(raw/'heartbreaker.png')
    preview=Image.new('RGBA',(448,176),(12,24,31,255))
    for x,size in ((24,128),(192,80),(320,48)):
        glyph=render_glyph();tinted=Image.new('RGBA',glyph.size,(77,225,229,255));tinted.putalpha(glyph.getchannel('A'))
        preview.alpha_composite(tinted.resize((size,size),Image.Resampling.LANCZOS),(x,(176-size)//2))
    preview.save(work/'preview.png')
    part={'$type':'inkTextureAtlasMapper','partName':cname('heartbreaker'),
          'clippingRectInUVCoords':{'$type':'RectF','Left':0.0,'Top':0.0,'Right':50/256,'Bottom':65/256}}
    glyph_part={'$type':'inkTextureAtlasMapper','partName':cname('velvet_crash'),
          'clippingRectInUVCoords':{'$type':'RectF','Left':128/256,'Top':0.0,'Right':160/256,'Bottom':32/256}}
    slots=[]
    for name in ('heartbreaker','heartbreaker_1080p','heartbreaker_1080p'):
        texture={'DepotPath':{'$type':'ResourcePath','$storage':'string','$value':rf'mod\gq004\ui\{name}.xbm'},'Flags':'Soft'}
        slots.append({'$type':'inkTextureSlot','texture':texture,'parts':[copy.deepcopy(part),copy.deepcopy(glyph_part)]})
    document={'Header':{'WolvenKitVersion':'8.17.4','WKitJsonVersion':'0.0.9','GameVersion':2310,
        'ExportedDateTime':'1970-01-01T00:00:00Z','DataType':'CR2W','ArchiveFileName':str(archive/'heartbreaker.inkatlas')},
        'Data':{'Version':195,'BuildVersion':0,'RootChunk':{'$type':'inkTextureAtlas','cookingPlatform':'PLATFORM_PC',
                  'slots':{'Elements':slots}}}}
    atlas=raw/'heartbreaker.inkatlas.json';atlas.write_text(json.dumps(document,indent=2)+'\n',encoding='utf-8')
    writer=str(resolve_tool('wolvenkit'))
    for name,command in [('atlas',[writer,'cr2w',str(atlas),'-d','-o',str(archive),'-v','Minimal']),
                         ('texture',[writer,'import',str(raw),'-o',str(archive)]),
                         ('readback',[writer,'cr2w',str(archive),'-s','-o',str(work/'readback'),'-v','Minimal'])]:
        result=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',errors='replace')
        (work/(name+'.log')).write_text(result.stdout+result.stderr,encoding='utf-8')
        imported=name=='texture' and result.returncode==3 and 'Imported 2/2 file(s)' in result.stdout
        if result.returncode and not imported:raise RuntimeError(f'Icon {name} failed: {work/(name+".log")}')
    actual=json.loads((work/'readback/heartbreaker.inkatlas.json').read_text(encoding='utf-8'))
    from build_world import verify_document
    report=verify_document(document,actual,json.loads((ROOT/'red-schema.json').read_text(encoding='utf-8')))
    assert report['ok'],report['errors']
    assert (archive/'heartbreaker.xbm').read_bytes()[:4]==b'CR2W'
    for name,expected in (('heartbreaker',image.resize((512,512),Image.Resampling.LANCZOS)),('heartbreaker_1080p',image)):
        texture_read=json.loads((work/f'readback/{name}.xbm.json').read_text(encoding='utf-8'))['Data']['RootChunk']
        assert (texture_read['width'],texture_read['height'])==expected.size
        buffer=base64.b64decode(texture_read['renderTextureResource']['renderResourceBlobPC']['Data']['textureData']['Bytes'])
        # WolvenKit flips PNG rows for engine UVs. Preserve chip colours as
        # well as alpha; a white-only glyph could not expose channel errors.
        pixels=ImageOps.flip(expected).tobytes()
        assert buffer[:len(pixels)]==pixels
    report['texture_alpha_preserved']=True
    report['texture_rgba_preserved_both_resolutions']=True
    (work/'validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print('Heartbreaker icon atlas and texture cooked; authored atlas fields verified.')


if __name__=='__main__':main()
