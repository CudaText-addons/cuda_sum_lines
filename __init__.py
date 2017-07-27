from cudatext import *

class Command:
    def get_sum(self, lines):
        nums = []
        bads = []

        #ignore empty/spaces
        lines = [s for s in lines if s.strip()]

        for (i, s) in enumerate(lines):
            try:
                num = float(s)
                nums += [num]
            except:
                bads += ['  - selection line '+str(i+1)+': '+s]

        eol = '\n'
        res = ''

        if nums:
            res += 'Sum: ' + str(sum(nums)) + eol
            res += 'Min: ' + str(min(nums)) + eol
            res += 'Max: ' + str(max(nums)) + eol
            res += 'Avg: ' + str(sum(nums) / float(len(nums))) + eol

        res += 'Numbers processed: ' + str(len(nums)) + eol
        res += 'Lines processed: ' + str(len(lines)) + eol
        if bads:
            res += 'Lines skipped: ' + str(len(bads)) + eol + eol.join(bads) + eol
        return res

    def run(self):

        mode = ed.get_sel_mode()
        if mode==SEL_NORMAL:
            text = ed.get_text_sel()
            if not text:
                msg_status('Text not selected')
                return
            lines = text.splitlines()

            n1, n2 = ed.get_sel_lines()
            caption = 'Normal selection: lines %d..%d' % (n1+1, n2+1)

        elif mode==SEL_COLUMN:
            lines = []
            x1, y1, x2, y2 = ed.get_sel_rect()
            for i in range(y1, y2+1):
                s = ed.get_text_line(i)
                s = s[x1:x2]
                print('"'+s+'"')
                lines.append(s)

            caption = 'Column selection: lines %d..%d, columns %d..%d' % (y1+1, y2+1, x1+1, x2+1)

        else:
            return

        text = self.get_sum(lines)
        if not text:
            msg_status('Sum Lines: empty result')
            return

        text = caption+'\n\n'+text

        file_open('')
        ed.set_prop(PROP_TAB_TITLE, 'Sum Lines')
        ed.insert(0, 0, text)
