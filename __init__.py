from cudatext import *

class Command:
    def run(self):
        text = ed.get_text_sel()
        if not text:
            msg_status('Text not selected')
            return 
        n1, n2 = ed.get_sel_lines()
        
        nums = []
        bads = []
        for n in range(n1, n2+1):
            s = ed.get_text_line(n)
            if not s: continue
            try:
                num = float(s)
                nums += [num]
            except:
                bads += ['  Line '+str(n+1)+': '+s]
            
        file_open('')
        eol = '\n'
        
        res = ''
        res += 'Sum: ' + str(sum(nums)) + eol
        res += 'Min: ' + str(min(nums)) + eol
        res += 'Max: ' + str(max(nums)) + eol
        res += 'Avg: ' + str(sum(nums) / float(len(nums))) + eol

        res += 'Nums counted: ' + str(len(nums)) + eol
        res += 'Lines processed: ' + str(n2-n1+1) + eol
        if bads:
            res += 'Lines skipped: ' + str(len(bads)) + eol + eol.join(bads) + eol

        x0, y0, x1, y1 = ed.get_carets()[0]             
        ed.insert(x0, y0, res)
